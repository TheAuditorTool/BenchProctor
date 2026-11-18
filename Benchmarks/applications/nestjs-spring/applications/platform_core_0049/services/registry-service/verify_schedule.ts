// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("registry-service")
export class VerifySchedule {
  @Post("verifySchedule")
  async verifySchedule(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers.referer as string) || "";
    const persona = notice != null ? notice : '';
    const fileContent = fs.readFileSync("/var/app/data/" + persona, "utf8");
    return fileContent;
  }
}
