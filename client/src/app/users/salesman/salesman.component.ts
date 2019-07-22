import 'rxjs/Rx';
import { CommonService } from "./../../shared/common.service"
import { Http } from '@angular/http';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-salesman',
  templateUrl: './salesman.component.html',
  styleUrls: ['./salesman.component.css']
})
export class SalesmanComponent implements OnInit {
data: any = null;
endpoint = '/users/salesman/';
  constructor(private http: Http, private _service: CommonService) {

  }

  ngOnInit() {
  }

  onSubmit = function(my_form: any){
        this._service.postForm(this.endpoint, my_form)
            .subscribe(
            data => {
              console.log("data posted", data);
            });
  };

  get_data = function(){
        this._service.getData(this.endpoint, this.tenant_id)
            .subscribe((response) => {
        console.log("API sent", response);
      });
  };
}
