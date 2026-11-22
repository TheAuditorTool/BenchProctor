// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("asset-library")
export class AttachAsset {
  @Post("attachAsset")
  async attachAsset(@Req() req: Request): Promise<unknown> {
    const remark = req.body.publishing_payload || "";
    const fileContent = fs.readFileSync("/var/app/data/" + remark, "utf8");
    return fileContent;
  }
}
