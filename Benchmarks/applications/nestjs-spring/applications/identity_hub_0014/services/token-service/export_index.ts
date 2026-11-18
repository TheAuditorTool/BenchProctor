// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("token-service")
export class ExportIndex {
  @Post("exportIndex")
  async exportIndex(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers.referer as string) || "";
    const persona = snippet != null ? snippet : '';
    const fileContent = fs.readFileSync("/var/app/data/" + persona, "utf8");
    return fileContent;
  }
}
