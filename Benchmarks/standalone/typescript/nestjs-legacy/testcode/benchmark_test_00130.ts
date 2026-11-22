// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as fs from "fs";
import * as nodeUtil from "util";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";
import * as zod from "zod";
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
  @Post("BenchmarkTest00130")
  async BenchmarkTest00130(@Headers("x-custom-header") hdr: string): Promise<unknown> {
    const userInput = hdr || "";
    const data = nodeUtil.format("%s", userInput);
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%~\-]+$/).safeParse(String(data));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const processed = _parsed.data;
    const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
    xpath.evaluate("//user[name='" + processed + "']", usersDoc, null, xpath.XPathResult.ANY_TYPE, null);
    return { created: true };
  }
}
