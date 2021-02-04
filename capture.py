import cv2

WIDTH = 640
HEIGHT = 480

if __name__ == "__main__":
    # Open the web cam
    cap = cv2.VideoCapture(0)

    # Set the width and height
    cap.set(3, WIDTH)
    cap.set(4, HEIGHT)

    # Recorder
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter("output.mp4",
                                   fourcc,
                                   30,
                                   (WIDTH, HEIGHT)
                                   )

    if not cap.isOpened():
        print("Camera not opened")
        exit(1)

    # record video
    while True:
        success, frame = cap.read()
        if success:
            video_writer.write(frame)
            cv2.imshow('Video', frame)

        if cv2.waitKey(40) == 27:  # ESC
            break

    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()
