// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("billing-api")
export class LoadRoster {
  @Post("loadRoster")
  async loadRoster(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.referer as string) || "";
    const remittance = remark != null ? remark : '';
    const fileContent = fs.readFileSync("/var/app/data/" + remittance, "utf8");
    return fileContent;
  }
}
