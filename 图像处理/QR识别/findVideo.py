import cv2


def find_qr_code_from_camera():
    # 打开到摄像头的连接（0 是默认摄像头）
    cap = cv2.VideoCapture(0)

    while True:
        # 从摄像头读取一帧图像
        ret, frame = cap.read()

        if not ret:
            print("错误：无法从摄像头捕获图像。")
            break

        # 将图像转换为灰度
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 使用OpenCV自带的Sobel算子进行过滤
        gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
        gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

        # 将过滤得到的X方向像素值减去Y方向的像素值
        gradient = cv2.subtract(gradX, gradY)
        # 先缩放元素再取绝对值，最后转换格式为8bit型
        gradient = cv2.convertScaleAbs(gradient)
        # 均值滤波取二值化
        blurred = cv2.blur(gradient, (15, 15))  # 增加均值滤波核的大小
        (_, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)  # 调整阈值

        # 腐蚀和膨胀的函数
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))  # 增大形态学操作的内核大小
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        closed = cv2.erode(closed, None, iterations=4)
        closed = cv2.dilate(closed, None, iterations=4)

        # 找到边界findContours函数
        (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 计算出包围目标的最小矩形区域
        for c in cnts:
            epsilon = 0.04 * cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, epsilon, True)

            if len(approx) >= 4:  # 调整顶点数的最小阈值
                # 在QR码周围绘制边界框
                cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)

        # 显示帧
        cv2.imshow("QR码检测", frame)

        # 当按下 'q' 键时退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放摄像头并关闭所有窗口
    cap.release()
    cv2.destroyAllWindows()


# 调用函数以开始从摄像头进行QR码检测
find_qr_code_from_camera()
