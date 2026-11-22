// SPDX-License-Identifier: Apache-2.0
import { Controller, Param, Post } from "@nestjs/common";
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
  @Post("BenchmarkTest00347/:id")
  async BenchmarkTest00347(@Param("id") pathId: string): Promise<unknown> {
    const userInput = pathId;
    const data = nodeUtil.format("%s", userInput);
    const minstd = { state: (Date.now() % 2147483646) + 1, next() { this.state = (this.state * 48271) % 2147483647; return this.state; } };
    const token = minstd.next().toString(36) + minstd.next().toString(36) + "-" + String(data).slice(0, 8);
    return { token };
  }
}
