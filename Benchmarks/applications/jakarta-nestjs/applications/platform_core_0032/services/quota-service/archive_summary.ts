// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("quota-service")
export class ArchiveSummary {
  @Post("archiveSummary")
  async archiveSummary(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.referer as string) || "";
    const payload = { get value() { return remark; } };
    const persona = payload.value;
    const fileContent = fs.readFileSync("/var/app/data/" + persona, "utf8");
    return fileContent;
  }
}
