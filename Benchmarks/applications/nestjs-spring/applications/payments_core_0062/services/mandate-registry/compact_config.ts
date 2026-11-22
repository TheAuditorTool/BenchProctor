// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("mandate-registry")
export class CompactConfig {
  @Post("compactConfig")
  async compactConfig(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers["user-agent"] as string) || "";
    let disbursement;
    try { disbursement = JSON.parse(headline).value || headline; }
    catch (e) { disbursement = headline; }
    const remittance = "/var/app/data/" + path.basename(disbursement);
    const fileContent = fs.readFileSync(remittance, "utf8");
    return fileContent;
  }
}
