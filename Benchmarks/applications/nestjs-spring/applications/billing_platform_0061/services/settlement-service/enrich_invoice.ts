// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("settlement-service")
export class EnrichInvoice {
  @Post("enrichInvoice")
  async enrichInvoice(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["user-agent"] as string) || "";
    let remittance;
    try { remittance = JSON.parse(footnote).value || footnote; }
    catch (e) { remittance = footnote; }
    const arrears = "/var/app/data/" + path.basename(remittance);
    const fileContent = fs.readFileSync(arrears, "utf8");
    return fileContent;
  }
}
