#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QPainter>
#include <QTimer>
#include <ctime>
#include <vector>

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = 0);
    ~Widget();

private:
    Ui::Widget *ui;
    QTimer *t1;
    QStringList nameList;
    int posX;
    void paintEvent(QPaintEvent *event);
    void writeName();
    void initConnect();

};

#endif // WIDGET_H
