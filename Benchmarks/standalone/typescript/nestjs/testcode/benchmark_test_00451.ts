// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post } from "@nestjs/common";
import { Response } from "express";
import * as libxmljs from "libxmljs";
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
  @Post("BenchmarkTest00451")
  async BenchmarkTest00451(@Body("field") field: string): Promise<unknown> {
    const userInput = field || "";
    const data = decodeURIComponent(userInput);
    libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false } as libxmljs.XMLParseOptions);
    return { created: true };
  }
}
