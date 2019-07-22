import { Component, OnInit, NgModule } from '@angular/core';
import {RouterModule} from "@angular/router";

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {
public show_content = false;
  constructor(
  ) { }

  ngOnInit() {
  }

}
