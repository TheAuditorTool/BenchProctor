// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("archive-store")
export class MergeLedger {
  @Post("mergeLedger")
  async mergeLedger(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.host as string) || "";
    const addendum = wording != null ? wording : '';
    if (!/^(asc|desc|name|created)$/.test(String(addendum))) { throw new BadRequestException({error:"invalid"}); }
    const dossier = addendum;
    fs.writeFileSync("/var/uploads/" + dossier, "data");
    return { created: true };
  }
}
