import 'rxjs/Rx';
import { BuyerService } from "./shared/buyer.service"
import { Http } from '@angular/http';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-buyer',
  templateUrl: './buyer.component.html',
  styleUrls: ['./buyer.component.css']
})
export class BuyerComponent implements OnInit {
  data: any = null;
  constructor(private http: Http, private _buyerService: BuyerService) {

  }

  ngOnInit() {
  }

  onSubmit = function(my_form: any){
        this._buyerService.postBuyerForm(my_form)
            .subscribe(
            data => {
              console.log("data posted", data);
            });
  };

  get_data = function(my_form: any){
        this._buyerService.getData(5)
            .subscribe((response) => {
        console.log("API sent", response);
      });
  };
}
