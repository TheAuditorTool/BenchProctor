// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("log-shipper")
export class LoadSchedule {
  @Post("loadSchedule")
  async loadSchedule(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.referer as string) || "";
    const gauge = caption != null ? caption : '';
    const fileContent = fs.readFileSync("/var/app/data/" + gauge, "utf8");
    return fileContent;
  }
}
