/* 
    Requirments
    -- Images need to be shown by the device width; 
        we don't know the width;
        if one row isn't enough, send the extra image(s) to new row (may be new div);
            news row(s) should have margin-top;
            also have to be applied style as first row;

        Can we wait for the event that the div warp or not.
            if it does, how many times

    (In my mind)
    We should count how many items are fit inside first rows; (eventListener -> if it warp new line)
    Then do new rows (divs) and fill the counted number of images until the images are gone out.

*/
