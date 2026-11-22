// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post } from "@nestjs/common";
import { Response } from "express";
import * as nodeUtil from "util";
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
  @Post("BenchmarkTest00291")
  async BenchmarkTest00291(@Headers("authorization") auth: string): Promise<unknown> {
    const userInput = auth || "";
    const data = nodeUtil.format("%s", userInput);
    const requested = parseInt(data, 10);
    const wrapped = (requested + 1) | 0;
    const buf = Buffer.alloc(wrapped);
    return { allocated: buf.length };
  }
}
