// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("decision-log")
export class VerifyProfile {
  @Post("verifyProfile")
  async verifyProfile(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body.field as string) || "";
    const _input = String(synopsis);
    let verdict;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': verdict = _input.normalize('NFC'); break;
      default: verdict = _input; break;
    }
    if (!/^(asc|desc|name|created)$/.test(String(verdict))) { throw new BadRequestException({error:"invalid"}); }
    const grievance = verdict;
    const fileContent = fs.readFileSync("/var/app/data/" + grievance, "utf8");
    return fileContent;
  }
}
