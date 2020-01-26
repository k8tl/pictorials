from app import app

@app.route('/')
@app.route('/index')
def index():
        return render_template("public/upload_image.html")

@app.route('/lineart')
def lineArt(self, image):
        fullName = image
        src = cv.imread(image, cv.IMREAD_COLOR)
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        lines = lsd(gray)
        img = np.zeros([1080,1200,3],dtype=np.uint8)
        img.fill(255)
        os.mkdir('./lineart')
        for i in range(lines.shape[0]):
            pt1 = (int(lines[i, 0]), int(lines[i, 1]))
            pt2 = (int(lines[i, 2]), int(lines[i, 3]))
            width = lines[i, 4]
            cv.line(img, pt1, pt2, (0, 0, 0), int(np.ceil(width / 2)))
            if i%10==0 or i==lines.shape[0]-1:
                cv.imshow('Step', img)
                cv.waitKey(0)
                cv.destroyAllWindows()
                cv.imwrite('./gallery/new' + i + '.jpg', img)
	

