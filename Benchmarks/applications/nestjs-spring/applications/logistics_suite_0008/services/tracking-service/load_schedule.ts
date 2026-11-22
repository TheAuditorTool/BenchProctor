// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("tracking-service")
export class LoadSchedule {
  @Post("loadSchedule")
  async loadSchedule(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers["user-agent"] as string) || "";
    let consignment;
    try { consignment = JSON.parse(caption).value || caption; }
    catch (e) { consignment = caption; }
    const parcel = "/var/app/data/" + path.basename(consignment);
    const fileContent = fs.readFileSync(parcel, "utf8");
    return fileContent;
  }
}
