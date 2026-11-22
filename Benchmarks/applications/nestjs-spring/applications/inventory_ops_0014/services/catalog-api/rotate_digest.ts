// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("catalog-api")
export class RotateDigest {
  @Post("rotateDigest")
  async rotateDigest(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["user-agent"] as string) || "";
    let restock;
    try { restock = JSON.parse(excerpt).value || excerpt; }
    catch (e) { restock = excerpt; }
    const backorder = "/var/app/data/" + path.basename(restock);
    const fileContent = fs.readFileSync(backorder, "utf8");
    return fileContent;
  }
}
