// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("payments-api")
export class SummarizeManifest {
  @Post("summarizeManifest")
  async summarizeManifest(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.host as string) || "";
    const remittance = footnote != null ? footnote : '';
    if (!/^(asc|desc|name|created)$/.test(String(remittance))) { throw new BadRequestException({error:"invalid"}); }
    const disbursement = remittance;
    fs.writeFileSync("/var/uploads/" + disbursement, "data");
    return { created: true };
  }
}
