// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("convert-service")
export class FetchThreshold {
  @Post("fetchThreshold")
  async fetchThreshold(@Req() req: Request): Promise<unknown> {
    const citation = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(citation).split(',')) { parts.push(token); }
    const dossier: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(dossier))) { throw new BadRequestException({error:"invalid"}); }
    const addendum = dossier;
    fs.unlinkSync("/var/app/data/" + addendum);
    return { created: true };
  }
}
