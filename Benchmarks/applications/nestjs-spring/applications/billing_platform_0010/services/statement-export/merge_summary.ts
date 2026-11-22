// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("statement-export")
export class MergeSummary {
  @Post("mergeSummary")
  async mergeSummary(@Req() req: Request): Promise<unknown> {
    const headline = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const remittance: string = transform(headline);
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(remittance)) { throw new BadRequestException({error:"invalid"}); }
    const dunning = remittance;
    fs.writeFileSync("/var/uploads/" + dunning, "data");
    return { created: true };
  }
}
