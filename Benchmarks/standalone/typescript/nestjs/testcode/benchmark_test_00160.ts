// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
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
  @Post("BenchmarkTest00160")
  async BenchmarkTest00160(@Req() req: Request): Promise<unknown> {
    const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let data;
    try { data = JSON.parse(userInput).value || userInput; }
    catch (e) { data = userInput; }
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
    req.session.data = String(processed);
    return { created: true };
  }
}
