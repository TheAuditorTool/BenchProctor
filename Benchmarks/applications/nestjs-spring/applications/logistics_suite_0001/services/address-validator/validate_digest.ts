// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("address-validator")
export class ValidateDigest {
  @Post("validateDigest")
  async validateDigest(@Req() req: Request): Promise<unknown> {
    const quotation = (req.headers["user-agent"] as string) || "";
    let parcel;
    try { parcel = JSON.parse(quotation).value || quotation; }
    catch (e) { parcel = quotation; }
    const consignment = "/var/app/data/" + path.basename(parcel);
    const fileContent = fs.readFileSync(consignment, "utf8");
    return fileContent;
  }
}
