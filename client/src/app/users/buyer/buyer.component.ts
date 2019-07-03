import 'rxjs/Rx';
import { CommonService } from "./../../shared/common.service"
import { Http } from '@angular/http';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-buyer',
  templateUrl: './buyer.component.html',
  styleUrls: ['./buyer.component.css']
})
export class BuyerComponent implements OnInit {
  data: any = null;
  endpoint = '/users/buyer/';
  constructor(private http: Http, private _service: CommonService) {
  }

  ngOnInit() {
  }

  onSubmit = function(my_form: any){
        this._service.postForm(this.endpoint, my_form)
            .subscribe(
            data => {
              console.log("data posted", data);
              this.buyer_id = data.id;
              console.log("Buyer_ID of the saved data is :%s", this.buyer_id)
            });
  };

  get_data = function(){
        this._service.getData(this.endpoint)
            .subscribe((response) => {
        console.log("API sent", response);
      });
  };

}
