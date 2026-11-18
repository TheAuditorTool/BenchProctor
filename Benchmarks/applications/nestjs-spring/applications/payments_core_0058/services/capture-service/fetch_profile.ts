// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("capture-service")
export class FetchProfile {
  @Post("fetchProfile")
  async fetchProfile(@Req() req: Request): Promise<unknown> {
    const caption = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const ledger: string = normalize(caption);
    if (!/^(asc|desc|name|created)$/.test(String(ledger))) { throw new BadRequestException({error:"invalid"}); }
    const remittance = ledger;
    fs.unlinkSync("/var/app/data/" + remittance);
    return { created: true };
  }
}
