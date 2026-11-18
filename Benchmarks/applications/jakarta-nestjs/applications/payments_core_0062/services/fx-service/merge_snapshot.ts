// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("fx-service")
export class MergeSnapshot {
  @Post("mergeSnapshot")
  async mergeSnapshot(@Req() req: Request): Promise<unknown> {
    const headline = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return headline; } };
    const disbursement = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(disbursement))) { throw new BadRequestException({error:"invalid"}); }
    const remittance = disbursement;
    const fileContent = fs.readFileSync("/var/app/data/" + remittance, "utf8");
    return fileContent;
  }
}
