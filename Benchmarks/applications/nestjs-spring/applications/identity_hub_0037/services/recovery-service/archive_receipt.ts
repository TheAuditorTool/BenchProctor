// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("recovery-service")
export class ArchiveReceipt {
  @Post("archiveReceipt")
  async archiveReceipt(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers["user-agent"] as string) || "";
    let persona;
    try { persona = JSON.parse(remark).value || remark; }
    catch (e) { persona = remark; }
    const notice = "/var/app/data/" + path.basename(persona);
    const fileContent = fs.readFileSync(notice, "utf8");
    return fileContent;
  }
}
