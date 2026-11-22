// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("address-validator")
export class NormalizeWindow {
  @Post("normalizeWindow")
  async normalizeWindow(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers["user-agent"] as string) || "";
    let consignment;
    try { consignment = JSON.parse(citation).value || citation; }
    catch (e) { consignment = citation; }
    const parcel = "/var/app/data/" + path.basename(consignment);
    const fileContent = fs.readFileSync(parcel, "utf8");
    return fileContent;
  }
}
