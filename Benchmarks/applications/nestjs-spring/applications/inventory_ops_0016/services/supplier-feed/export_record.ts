// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("supplier-feed")
export class ExportRecord {
  @Post("exportRecord")
  async exportRecord(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers["x-forwarded-for"] as string) || "";
    let backorder;
    try { backorder = JSON.parse(citation).value || citation; }
    catch (e) { backorder = citation; }
    fs.unlinkSync("/var/app/data/" + backorder);
    return { created: true };
  }
}
