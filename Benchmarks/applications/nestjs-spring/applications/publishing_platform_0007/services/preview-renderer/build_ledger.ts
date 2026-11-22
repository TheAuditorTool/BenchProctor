// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("preview-renderer")
export class BuildLedger {
  @Post("buildLedger")
  async buildLedger(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers["user-agent"] as string) || "";
    let byline;
    try { byline = JSON.parse(remark).value || remark; }
    catch (e) { byline = remark; }
    const addendum = "/var/app/data/" + path.basename(byline);
    const fileContent = fs.readFileSync(addendum, "utf8");
    return fileContent;
  }
}
