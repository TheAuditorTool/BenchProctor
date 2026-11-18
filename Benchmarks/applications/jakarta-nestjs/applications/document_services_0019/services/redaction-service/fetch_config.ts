// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("redaction-service")
export class FetchConfig {
  @Post("fetchConfig")
  async fetchConfig(@Req() req: Request): Promise<unknown> {
    const passage = (req.body.field as string) || "";
    const _input = String(passage);
    let dossier;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': dossier = _input.normalize('NFC'); break;
      default: dossier = _input; break;
    }
    if (!/^(asc|desc|name|created)$/.test(String(dossier))) { throw new BadRequestException({error:"invalid"}); }
    const addendum = dossier;
    const fileContent = fs.readFileSync("/var/app/data/" + addendum, "utf8");
    return fileContent;
  }
}
