// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("capture-service")
export class EnrichWallet {
  @Post("enrichWallet")
  async enrichWallet(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.referer as string) || "";
    const formData = Object.freeze({ payload: footnote });
    const remittance = formData.payload;
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(remittance)) { throw new BadRequestException({error:"invalid"}); }
    const disbursement = remittance;
    fs.writeFileSync("/var/uploads/" + disbursement, "data");
    return { created: true };
  }
}
