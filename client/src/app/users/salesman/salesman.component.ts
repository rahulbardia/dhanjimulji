import 'rxjs/Rx';
import { SalesmanService } from "./shared/salesman.service"
import { Http } from '@angular/http';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-salesman',
  templateUrl: './salesman.component.html',
  styleUrls: ['./salesman.component.css']
})
export class SalesmanComponent implements OnInit {
data: any = null;
  constructor(private http: Http, private _service: SalesmanService) {

  }

  ngOnInit() {
  }

  onSubmit = function(my_form: any){
        this._service.postForm(my_form)
            .subscribe(
            data => {
              console.log("data posted", data);
            });
  };

  get_data = function(my_form: any){
        this._service.getData(5)
            .subscribe((response) => {
        console.log("API sent", response);
      });
  };
}
