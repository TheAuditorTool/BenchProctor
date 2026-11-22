// SPDX-License-Identifier: Apache-2.0
import { Controller, Param, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as fs from "fs";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";
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
  @Post("BenchmarkTest00325/:id")
  async BenchmarkTest00325(@Param("id") pathId: string): Promise<unknown> {
    const userInput = pathId;
    const pending: string[] = String(userInput).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const data: string = collected.join(',');
    class PayloadRules {
      @IsString()
      @Matches(/^[a-zA-Z0-9 _.%~\-]+$/)
      value!: string;
    }
    const _rules = new PayloadRules();
    _rules.value = String(data);
    const _violations = validateSync(_rules);
    if (_violations.length > 0) { throw new BadRequestException({error:"invalid"}); }
    const processed = _rules.value;
    const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
    xpath.parse("//user[name='" + processed + "']").select({ node: usersDoc });
    return { created: true };
  }
}
