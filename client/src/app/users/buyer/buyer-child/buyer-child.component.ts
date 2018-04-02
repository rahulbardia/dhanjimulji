import 'rxjs/Rx';
import { CommonService } from "./../../../shared/common.service"
import { Http } from '@angular/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-buyer-child',
  templateUrl: './buyer-child.component.html',
  styleUrls: ['./buyer-child.component.css']
})
export class BuyerChildComponent implements OnInit {
  data: any = null;
  endpoint = '/users/buyerchild/';
  constructor(private http: Http, private _buyerService: CommonService) {
  }

  ngOnInit() {
  }

  onSubmit = function(my_form: any){
        this._buyerService.postForm(this.endpoint, my_form)
            .subscribe(
            data => {
              console.log("data posted", data);
            });
  };

  get_data = function(my_form: any){
        this._buyerService.getData(this.endpoint, 5)
            .subscribe((response) => {
        console.log("API sent", response);
      });
  };
}
