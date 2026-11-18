// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("asset-library")
export class CollectSyndication {
  @Post("collectSyndication")
  async collectSyndication(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.referer as string) || "";
    const addendum = summary != null ? summary : '';
    const fileContent = fs.readFileSync("/var/app/data/" + addendum, "utf8");
    return fileContent;
  }
}
