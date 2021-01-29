#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget),
    posX(0),
    t1(NULL)
{
    ui->setupUi(this);

//    connect(ui->btn_move, &QPushButton::clicked, [=](){
//        posX += 20;
//        update();
//    });

    if(t1 == NULL)
    {
        t1 = new QTimer(this);
    }


    writeName();
    initConnect();

}

void Widget::writeName()
{
    nameList << "张三" << "李四" << "王五" << "赵六";
}

void Widget::initConnect()
{
    connect(ui->btn_start,&QPushButton::clicked, [=](){
        t1->start(500);
    });
    connect(ui->btn_stop,&QPushButton::clicked, [=](){
        t1->stop();
    });

    connect(t1, &QTimer::timeout, [=](){
        //update();
        //qsrand((unsigned) time(0));
        qsrand(qrand());
        int num = qrand()%4;
        QString name = nameList.at(num);

        ui->label->setText(name);
        QFont ft;
        ft.setPointSize(20);
        ui->label->setFont(ft);
        ui->label->setAlignment(Qt::AlignCenter);
        t1->start(500);
    });
}


void Widget::paintEvent(QPaintEvent *event)
{

    //利用画家 画资源图片
    QPainter painter(this);

    if(posX > this->width()-50)
    {
        posX = 0;
    }

    painter.drawPixmap(posX, 100, QPixmap(":/image/jingxiuxiu.jpg"));


}




Widget::~Widget()
{
    delete ui;
}
