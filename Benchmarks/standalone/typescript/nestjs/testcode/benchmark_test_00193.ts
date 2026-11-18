// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";
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
  @Post("BenchmarkTest00193")
  async BenchmarkTest00193(@Body("field") field: string): Promise<unknown> {
    const userInput = field || "";
    const data = `${userInput}`;
    if (!/^(asc|desc|name|created)$/.test(String(data))) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
    xpath.select("//user[name='" + processed + "']", xmlDoc);
    return { created: true };
  }
}
