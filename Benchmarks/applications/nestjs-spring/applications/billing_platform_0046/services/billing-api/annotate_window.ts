// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("billing-api")
export class AnnotateWindow {
  @Post("annotateWindow")
  async annotateWindow(@Req() req: Request): Promise<unknown> {
    const remark = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const remittance: string = normalize(remark);
    if (!/^(asc|desc|name|created)$/.test(String(remittance))) { throw new BadRequestException({error:"invalid"}); }
    const arrears = remittance;
    fs.unlinkSync("/var/app/data/" + arrears);
    return { created: true };
  }
}
