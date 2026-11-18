// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("manifest-builder")
export class AuditHeader {
  @Post("auditHeader")
  async auditHeader(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers["x-custom-header"] as string) || "";
    const parcel = String(citation).split(/[ \t]+/).join(" ");
    fs.unlinkSync("/var/app/data/" + parcel);
    return { created: true };
  }
}
