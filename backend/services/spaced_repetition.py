from datetime import datetime,timedelta



INTERVALS={

1:1,

2:3,

3:7,

4:14,

5:30

}



def update_box(
        current_box,
        correct
):


    if correct:

        new_box=min(
            current_box+1,
            5
        )

    else:

        new_box=1



    next_date=datetime.now()+timedelta(

        days=INTERVALS[new_box]

    )


    return new_box,next_date