// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as nodeUtil from "util";
import { IsString, Matches, validateSync } from "class-validator";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00319")
  async BenchmarkTest00319(@Req() req: Request): Promise<unknown> {
    const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const data = nodeUtil.format("%s", userInput);
    class PayloadRules {
      @IsString()
      @Matches(/^[a-zA-Z0-9 _.\-]+$/)
      value!: string;
    }
    const _rules = new PayloadRules();
    _rules.value = String(data);
    const _violations = validateSync(_rules);
    if (_violations.length > 0) { throw new BadRequestException({error:"invalid"}); }
    const processed = _rules.value;
    req.app.locals.announcement = String(processed);
    return { created: true };
  }
}
