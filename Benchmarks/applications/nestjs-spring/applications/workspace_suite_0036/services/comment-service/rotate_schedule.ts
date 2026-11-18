// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("comment-service")
export class RotateSchedule {
  @Post("rotateSchedule")
  async rotateSchedule(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.referer as string) || "";
    const synopsis = remark != null ? remark : '';
    const fileContent = fs.readFileSync("/var/app/data/" + synopsis, "utf8");
    return fileContent;
  }
}
