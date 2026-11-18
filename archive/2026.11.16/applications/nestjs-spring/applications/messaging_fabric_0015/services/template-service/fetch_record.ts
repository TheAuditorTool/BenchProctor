// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("template-service")
export class FetchRecord {
  @Post("fetchRecord")
  async fetchRecord(@Req() req: Request): Promise<unknown> {
    const heading = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const bulletin: string = normalize(heading);
    if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { throw new BadRequestException({error:"invalid"}); }
    const excerpt = bulletin;
    childProcess.execSync("echo " + excerpt);
    return { created: true };
  }
}
