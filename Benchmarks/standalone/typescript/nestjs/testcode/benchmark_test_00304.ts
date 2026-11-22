// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as nodeUtil from "util";
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
  @Post("BenchmarkTest00304")
  async BenchmarkTest00304(@Headers("origin") origin: string): Promise<unknown> {
    const userInput = origin || "";
    const data = nodeUtil.format("%s", userInput);
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
    const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
    xpath.select("//user[name='" + processed + "']", xmlDoc);
    return { created: true };
  }
}
