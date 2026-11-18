// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("config-service")
export class RotateBatch {
  @Post("rotateBatch")
  async rotateBatch(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers["x-custom-header"] as string) || "";
    const persona = String(notice).split(/[ \t]+/).join(" ");
    fs.unlinkSync("/var/app/data/" + persona);
    return { created: true };
  }
}
