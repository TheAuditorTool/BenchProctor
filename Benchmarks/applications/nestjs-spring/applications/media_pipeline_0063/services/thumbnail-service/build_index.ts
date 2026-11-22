// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import { IsString, Matches, validateSync } from "class-validator";

@Controller("thumbnail-service")
export class BuildIndex {
  @Post("buildIndex")
  async buildIndex(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers["user-agent"] as string) || "";
    const montage = snippet != null ? snippet : '';
    class PayloadRules {
      @IsString()
      @Matches(/^[a-zA-Z0-9 _.%\-]+$/)
      value!: string;
    }
    const _rules = new PayloadRules();
    _rules.value = String(montage);
    const _violations = validateSync(_rules);
    if (_violations.length > 0) { throw new BadRequestException({error:"invalid"}); }
    const rendition = _rules.value;
    childProcess.exec("echo " + rendition, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
