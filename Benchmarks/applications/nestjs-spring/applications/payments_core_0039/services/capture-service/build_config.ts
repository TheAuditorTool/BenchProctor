// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("capture-service")
export class BuildConfig {
  @Post("buildConfig")
  async buildConfig(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers["user-agent"] as string) || "";
    let ledger;
    try { ledger = JSON.parse(memo).value || memo; }
    catch (e) { ledger = memo; }
    const remittance = "/var/app/data/" + path.basename(ledger);
    const fileContent = fs.readFileSync(remittance, "utf8");
    return fileContent;
  }
}
